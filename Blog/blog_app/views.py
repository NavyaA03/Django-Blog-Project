from django.shortcuts import render,get_object_or_404
from blog_app.models import post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag
# Create your views here.

def post_listView(request,tag_slug = None):
    posts = post.objects.all()

    #below 4 lines to handle tagging, if user clicks on tag
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug) #get tag from tags model, if we skip this n just compare tags of post with tag_slug. it will throw error tht tagable manager is not iterable
        posts = posts.filter(tags__in=[tag])

    #code to include pagination
    paginator_obj = Paginator(posts,2) #posts will have all the post, display 2per page. Paginator is a class
    page_number = request.GET.get('page') #fetching page number specified in url & stored in page_number attribute
    try:
        posts = paginator_obj.page(page_number) #retriving page number specfied by page_number
    except PageNotAnInteger:
        posts = paginator_obj.page(1) #if page number is not given , display first page. this will be executed when we just give /localhost
    except EmptyPage:
        posts = paginator_obj.page(paginator_obj.num_pages) #if localhost/200 is given & oly 10 pages are there, then it will display last page

    return render(request,'blog_app/post_list.html',{'posts':posts,'tag':tag})

# def detailed_view(request,slug_post):
#     post_detail = get_object_or_404(post,slug=slug_post)
#     return render(request,'blog_app/detail.html',{'post_detail':post_detail})

def detailed_view(request,year,month,day,slug_post):
    post_detail = get_object_or_404(post,slug=slug_post,
                                         publish__year = year,
                                         publish__month = month,
                                         publish__day = day,
                                         status = "published")
    comments = post_detail.Comments.filter(Active = True) #get all comments using related_name in model Comment
    comment_submit = False

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():

            #in form we have name,mail & comment to be filled by user, created update & active will be auto filled
            #so remaining post has to be assigned with current post & then save it
            new_comment = form.save(commit=False)
            new_comment.post = post_detail
            new_comment.save()
            comment_submit = True
    else:
        form = forms.CommentForm()

    return render(request,'blog_app/detail.html',{'post_detail':post_detail,"form":form,"comment_submit":comment_submit,"comments":comments})


from django.core.mail import send_mail
from . import forms

def EmailSending_View(request,id):

    post_data =get_object_or_404(post,id=id,status="published")
    sent = False #to differeciate response in html, flase = display form , true = email sent
    if request.method == "POST":  #when we click send email after filling form
        form = forms.EmailSending_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #configure subject
            subject = "{} recommends you to read '{}' blog".format(data['name'],post_data.title)
            #get url of blog to send in message
            #post_data.get_absolute_url returns url configured
            # build_absolute_uri returns http://127.0.0.1:8000/, which makes full url of blog(as same as blog detail)
            url = request.build_absolute_uri(post_data.get_absolute_url())
            # url = "http://127.0.0.1:8000/2020/12/30/python-interview-questions/"
            message = "Read post at {}\n\n {}'s comment is:\n {}".format(url,data['name'],data['Comment'])
            send_mail(subject,message,"Navya",[data['To_Mail']])
            sent = True

    else: #when we click on hyper link (send blog as email),it is always a GET. that is how we differeciate in view function
        form = forms.EmailSending_form()

    return render(request,"blog_app/sendemail.html",{"form":form,"post":post_data,"sent":sent})

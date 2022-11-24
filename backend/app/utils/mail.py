from app.common.config import MAIL_SENDER, MAIL_PASSWARD
from app.database.models import Post
from app.common.config import BACKEND_SERVER_URL
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_mail_content_by_post(post: Post, user_id: str) -> str:
    env = Environment(
        loader=FileSystemLoader('app/templates/'),
        autoescape=select_autoescape(['html']),
    )
    template = env.get_template("new_post_notice2.html")
    return template.render(
        user=post.user,
        title=post.title,
        link=post.link,
        BACKEND_SERVER_URL=BACKEND_SERVER_URL,
        user_id=user_id,
        short_description=post.short_description or "이 글의 요약을 가져오지 못했습니다. (2022.11.21 이전 글 일 가능성이 있습니다.)",
        user_img=post.user_img,
        released_year=post.created_at.year,
        released_month=post.created_at.month,
        released_day=post.created_at.day
    )


def send_post_notice_email(receiver_address: str, post: Post, user_id: str) -> None:
    mail_content = get_mail_content_by_post(post, user_id)
    message = MIMEMultipart()
    message['From'] = MAIL_SENDER
    message['To'] = receiver_address
    message['Subject'] = f"{post.title} | 새 글 알림"
    message.attach(MIMEText(mail_content, 'html'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(MAIL_SENDER, MAIL_PASSWARD)
    text = message.as_string()
    session.sendmail(MAIL_SENDER, receiver_address, text)
    session.quit()
    print('Mail Sent', receiver_address, post.title)

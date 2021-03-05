import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import sample
from string import ascii_uppercase

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.text import slugify

GENERAL_EMAIL_CORE = "atendimento@agronamesa.com.br"


def create_template(text_prop):
    return f'''
    <body
  style="
    background: url(https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Ftextura_bg.png?alt=media&token=dbec4086-92b1-4ab0-9f7b-f99387ef1dfc);
    background-repeat: repeat;
    margin: 0;
    justify-content: center;
  "
>
  <div
    style="
      background: url(https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Ftextura_bg_marrom.png?alt=media&token=80f794c6-1e2d-4f51-bd11-1c2e7797d9f5);
      background-repeat: repeat;
      height: 32px;
    "
  ></div>
  <div
    style="
      background: url(https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Ftextura_bg.png?alt=media&token=dbec4086-92b1-4ab0-9f7b-f99387ef1dfc);
      background-repeat: repeat;
      justify-content: center;
    "
  >
    <div
      style="
        height: 84px;
        margin-top: 48px;
        background: url(https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2FGrupo%20171.png?alt=media&token=a649e066-2dfe-4287-a42c-268e9f9cc8db);
        background-repeat: no-repeat;
        background-position: center;
      "
    ></div>
    <h2
      style="
        text-align: center;
        color: #7aad13;
        font-family: Oswald, sans-serif !important;
        margin-bottom: 200px;
      "
    >
      {text_prop}
    </h2>
    <div
      style="
        background: #7aad13;
        font-family: Oswald, sans-serif !important;
        display: flex;
        grid-template-columns: auto auto;
      "
    >
      <div style="text-align: center; width: 100%; margin-right: 4px">
        <div
          style="
            height: 80px;
            margin-top: 48px;
            width: 100%;
            background: url(https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2FGrupo%20172.png?alt=media&token=6ca08262-6ece-43c9-975b-5330aeb671a5);
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
          "
        ></div>
        <p style="color: #fafcf8; font-size: 14px">
          2020 © Serviço de Apoio às Micro e Pequenas Empresas Bahia.
          <br />Central de Relacionamento Sebrae: 0800 570 0800.
        </p>
      </div>
      <div style="text-align: center; width: 100%; margin-right: 4px">
        <div
          style="
            height: 80px;
            margin-top: 48px;
            width: 100%;
            background: url(https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2FGrupo%202.png?alt=media&token=59496c04-fd9c-4056-ba1b-77019d4fc489);
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
          "
        ></div>
        <a
          href="mailto:atendimento@agronamesa.com.br"
          style="color: #fafcf8; font-size: 14px"
        >
          atendimento@agronamesa.com.br
        </a>

        <div style="justify-content: center; margin-top: 8px">
          <a style="text-decoration: none;" href="https://t.me/sebraebahia">
            <img
              style="width: 24px; margin-right: 8px"
              src="https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Ftelegram-icon.png?alt=media&token=c2c425c0-5444-41e9-9fb8-da3dc16985c6"
            />
          </a>
          <a
            href="https://www.linkedin.com/company/sebraebahia/?originalSubdomain=br"
          >
            <img
              style="width: 24px; margin-right: 8px"
              src="https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Flinkedin-icon.png?alt=media&token=c2c425c0-5444-41e9-9fb8-da3dc16985c6"
            />
          </a>
          <a style="text-decoration: none;" href="https://www.facebook.com/sebraebahia">
            <img
              style="width: 24px; margin-right: 8px"
              src="https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Ffacebook-icon.png?alt=media&token=c2c425c0-5444-41e9-9fb8-da3dc16985c6"
            />
          </a>
          <a style="text-decoration: none;" href="https://twitter.com/sebraebahia">
            <img
              style="width: 24px; margin-right: 8px"
              src="https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Ftwitter-icon.png?alt=media&token=c2c425c0-5444-41e9-9fb8-da3dc16985c6"
            />
          </a>
          <a style="text-decoration: none;" href="https://www.youtube.com/user/SebraeBahia">
            <img
              style="width: 24px; margin-right: 8px"
              src="https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2Fyoutube-icon.png?alt=media&token=c2c425c0-5444-41e9-9fb8-da3dc16985c6"
            />
          </a>
          <a style="text-decoration: none;" href="https://www.instagram.com/sebraebahia/">
            <img
              style="width: 24px; margin-right: 8px"
              src="https://firebasestorage.googleapis.com/v0/b/sebrae-agro-2020.appspot.com/o/general%2FInstagram.png?alt=media&token=3c63b419-92c5-46cd-b50d-e9f1581f418c"
            />
          </a>
        </div>
      </div>
    </div>
  </div>
</body>
    '''


def show_profile_body(profile):
    contacts = ""
    if profile.contact:
        contacts = f'''
        tel: {profile.contact.telephone}
        cel: {profile.contact.celphone}
        '''
    body = f'''
    <div>
        Para ver esse perfil não listado <a href="https://agronamesa.com.br/produtor/{profile.slug}">CLIQUE AQUI</a><br />
        nome: {profile.name}<br />
        email: {profile.user.email}<br />
        cpf: {profile.cpf}<br />
        sexo: {profile.gender}<br />
        nascimento: {profile.date_birth}<br />
        cidade: {profile.city}<br />
        {profile.code_type}: {profile.code}<br />
        apresentacao: {profile.commentary}<br />
        razão social: {profile.social_reason}<br />
        cep: {profile.zip_code}<br />
        endereco: {profile.address}<br />
        {contacts}
    </div>
    '''
    return body


def show_profile_body_complete(profile):
    contacts = ""
    if profile.contact:
        contato = profile.contact
        contacts = f'''
        Contatos:
        site: {contato.site}
        instagram: {contato.instagram}
        facebook: {contato.facebook}
        whatsapp: {contato.whatsapp}
        tel: {contato.telephone}
        cel: {contato.celphone}
        cep: {contato.zipCode}
        email: {contato.emailBusiness}
        endereço: {contato.addressBusiness}
        '''

    body = f'''
    <div>
        Para ver esse perfil não listado <a href="https://agronamesa.com.br/produtor/{profile.slug}">CLIQUE AQUI</a><br />
        nome: {profile.name}<br />
        sexo: {profile.gender}<br />
        nascimento: {profile.date_birth}<br />
        cidade: {profile.city}<br />
        cpf: {profile.cpf}<br />
        {profile.code}: {profile.code_type}<br />
        comentario: {profile.commentary}<br />
        banner: {profile.banner}<br />
        razão social: {profile.social_reason}<br />
        slug: {profile.slug}<br />
        cidades que atua: {', '.join(profile.cities.values_list('title', flat=True))}<br />
        produtos: {', '.join(profile.products.values_list('title', flat=True))}<br />

        {contacts}
    </div>
    '''
    return body


def send_mail_from_adss(subj, mail_content, sender, receiver_address):
    sender_address = 'agronamesasebrae@gmail.com'
    sender_pass = 'agronamesa20!'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subj

    # message.attach(MIMEText(mail_content, 'plain'))
    message.attach(MIMEText(create_template(mail_content), 'html'))
    # message.attach( MIMEText(mail_content, 'html'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


def send_mail_with_html(subj, body, sender, receiver_address):
    msg = EmailMultiAlternatives(
        subj,
        '',
        sender,
        receiver_address
    )
    msg.attach_alternative(create_template(body), "text/html")
    msg.send()


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def is_valid_password(password, confirm_password):
    if password != confirm_password:
        return False
    if len(password) < 6:
        return False
    has_uppercase = False
    for c in password:
        if c in ascii_uppercase:
            has_uppercase = True
            break
    return has_uppercase


def generate_random_password():
    return ''.join(sample(ascii_uppercase, 6))


def send_user_new_password_message(actor, new_password):
    try:
        body = '''
Olá, {},

Sua senha foi alterada para {} (letras maiúsculas).
Ao acessar a nossa plataforma, aconselhamos alterar a senha. Clique em: Ver Meu Perfil > Alterar Senha.

Atenciosamente,


Equipe, Sebrae - Agro na Mesa
        '''
        send_mail_with_html(
            'Sua senha foi alterada no Sebrae - Agro na Mesa.',
            body.format(actor.name, new_password),
            settings.EMAIL_DEFAULT_SENDER,
            [actor.user.email],
            # fail_silently=False,
        )
        print('===> Mensagem de senha alterada enviada para {} ({})'.format(
            actor.name, actor.user.email))
        return True
    except Exception as error:
        print('===> Erro no envio de mensagem de senha alterada para {} ({}): {}'.format(
            actor.name, actor.user.email, error))
        return False


def send_user_support_message(full_name, email, telephone, subject, message):
    body = f'''
    <div>
        Assunto: <strong>{subject}</strong><br />
        telefone:{telephone}<br />
        email: {email}<br />
        {full_name} enviou a seguinte mensagem:<br/>
        mensagem: {message}
    <div>
    '''
    try:
        send_mail_from_adss(
            'Ajuda & Suporte',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            GENERAL_EMAIL_CORE,
            # fail_silently=False,
        )
        print('===> Mensagem de ajuda/suporte enviada para geral@core.com')
        return True
    except Exception as error:
        print(
            '===> Erro no envio de mensagem de ajuda/suporte para geral@core: ' + str(error))
        return False


def send_new_producer_registered(new_profile):
    try:
        body = show_profile_body(new_profile)
        send_mail_from_adss(
            f'{new_profile.pk} Produtor Cadastrado',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            GENERAL_EMAIL_CORE,
            # fail_silently=False,
        )
        print('===> Mensagem de ajuda/suporte enviada para geral@core.com')
        return True
    except Exception as error:
        print(
            '===> Erro no envio de mensagem de ajuda/suporte para geral@core: ' + str(error))
        return False


def confirm_register(email):
    body = f'''
    Pronto! Agora é só manter os seus produtos e demais informações sempre atualizados e divulgar para todos os seus clientes, para que seja possível vender mais com a ajuda do site Agro na Mesa.
    Aproveite! Se tiver alguma dúvida, sugestão ou reclamação, entre em contato por meio do formulário do site <a href="https://agronamesa.com.br/fale-conosco">AQUI</a>.
    '''
    try:
        send_mail_with_html(
            'Site Agro Na Mesa: Você concluiu o seu cadastro!',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            [email],
            # fail_silently=False,
        )
        print('===> Mensagem de ajuda/suporte enviada para geral@core.com')
        return True
    except Exception as error:
        print(
            '===> Erro no envio de mensagem de ajuda/suporte para geral@core: ' + str(error))
        return False


def finish_register_mail_to_profile(email):
    body = f'''
    Obrigado por completar o cadastro de seu PERFIL no site Agro na Mesa.
    Agora só falta a liberação para que você possa divulgar os seus produtos.Deve acontecer em poucos dias. Você receberá um e-mail avisando quando o seu PERFIL for liberado no site.
    Para acessar o agro na mesa <a href="https://agronamesa.com.br/">CLIQUE AQUI</a>
    '''
    try:
        send_mail_with_html(
            'Site Agro Na Mesa: Você concluiu o seu cadastro!',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            [email],
            # fail_silently=False,
        )
        print('===> Mensagem de ajuda/suporte enviada para geral@core.com')
        return True
    except Exception as error:
        print(
            '===> Erro no envio de mensagem de ajuda/suporte para geral@core: ' + str(error))
        return False


def finish_register_mail_to_agro(profile):
    try:
        body = show_profile_body_complete(profile)
        send_mail_from_adss(
            f'{profile.pk} Produtor com Cadastro Concluído',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            GENERAL_EMAIL_CORE,
            # fail_silently=False,
        )
        # send_mail_with_html(
        #     f'{profile.pk} Produtor com Cadastro Concluído',
        #     body,
        #     settings.EMAIL_DEFAULT_SENDER,
        #     [email],
        #     fail_silently=False,
        # )
        print('===> Mensagem de ajuda/suporte enviada para geral@core.com')
        return True
    except Exception as error:
        print(
            '===> Erro no envio de mensagem de ajuda/suporte para geral@core: ' + str(error))
        return False


def product_awaiting_release(profile):
    try:
        body = f'''Um produtor cadastrou um novo segmento ou produto.
        Por favor, avalie se está adequado para entrar no site Agro na Mesa.
        <a href="https://agro-na-mesa.herokuapp.com/admin/users/Profile/{profile.pk}/change/">CLIQUE AQUI</a>'''
        send_mail_from_adss(
            f'Produto/Segmento aguardando liberação',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            GENERAL_EMAIL_CORE,
        )
        print('===> Mensagem de ajuda/suporte enviada para geral@core.com')
        return True
    except Exception as error:
        print(
            '===> Erro no envio de mensagem de ajuda/suporte para geral@core: ' + str(error))
        return False


def send_welcome_message(name, email):
    body = f'''
        <div style="text-align:center">
            <b>Temos boas novas: você concluiu o cadastro de seus DADOS BÁSICOS no site Agro na Mesa! Mas para começar a divulgar seus produtos, você precisa criar o seu PERFIL no segundo formulário e aguardar a liberação.</b>
        </div>
        <div/>
        <div style="text-align:center"><b>Se ainda não completou o cadastro do seu PERFIL, <a href="https://agronamesa.com.br/produtor/meu-perfil">CLIQUE AQUI</a>!</b></div>
    '''
    try:
        send_mail_with_html(
            'Site Agro Na Mesa: Primeira etapa do cadastro concluída!',
            body,
            settings.EMAIL_DEFAULT_SENDER,
            [email],
            # fail_silently=False,
        )
        print('===> Mensagem de Solicitação de parceria enviada para geral@core.com')
        return True
    except Exception as error:
        print('===> Erro no envio de mensagem de Solicitação de parceria para geral@core: ' + str(error))
        return False

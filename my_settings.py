DATABASES = {
    'default' : {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'wemarpple',
        'USER': 'wemarpple',
        'PASSWORD': 'wemarpple',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS':{
            "use_pure":True,
        }
    }
}

WEMARPPLE_SECRET = {
        'secret':'%gcY*%bcw2!m*//K[8b6*S/+L/r#LM-F>0~zT$<F{;0SH8YFjt',
        'exp_time': datetime.now() + timedelta(seconds = 60 * 60 * 24),
}

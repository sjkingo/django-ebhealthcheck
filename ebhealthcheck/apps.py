from django.apps import AppConfig

class EBHealthCheckConfig(AppConfig):
    name = 'ebhealthcheck'

    def ready(self):
        """
        Fix for the EB health check host header:

        https://aalvarez.me/posts/setting-up-elastic-beanstalk-health-checks-with-a-django-application/
        https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
        """

        from django.conf import settings
        import requests

        def get_ec2_instance_ip():
            try:
                ip = requests.get(
                    'http://169.254.169.254/latest/meta-data/local-ipv4',
                    timeout=0.01
                ).text
            except requests.exceptions.ConnectionError:
                return None
            return ip

        public_ip = get_ec2_instance_ip()
        if public_ip:
            settings.ALLOWED_HOSTS.append(public_ip)

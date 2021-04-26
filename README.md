# Program: GPU-Crawler
Description: Crawl ecommerce websites to check 30XX RTX GPU's are instock  

## Dependencies
1. Docker >= 20.10
2. docker-compose >= 1.25

# Credentials setup
1. I used AWS's SNS api to send SMS message. You would need to have created an [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) w/ an AWS account.  
2. After acquiring: (i) AWS_KEY_ID (ii) AWS_SECRET_ACCESS_KEY (iii) AWS_REGION, input the AWS cred's and cellphone number that will receive SMS message in the <code>~/Dockerfile</code> (line 11-13 & 16), respectively.  

3. Then proceed to run

## Steps to run:
1. <code>git clone https://github.com/ActIII03/GPU-Crawler </code>

2. <code> sudo docker-compose up </code>
3. Then check text-file for list of instock GPU cards

### Documentation
1. [scrapy](https://docs.scrapy.org/en/latest/) - web crawling framework
2. [AWS SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) - asynchronous communication
3. [Docker](https://docs.docker.com/reference/) - Docker daemon (PaaS) that uses OS-level virtualization

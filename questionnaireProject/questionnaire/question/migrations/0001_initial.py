# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-10 06:52
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名称', help_text='用户名', max_length=32)),
                ('password', models.CharField(help_text='管理员密码', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='参与问卷日期')),
                ('is_done', models.BooleanField(default=False, help_text='是否已经完成')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名称', help_text='客户名称', max_length=32)),
                ('email', models.CharField(blank=True, default='', help_text='邮箱', max_length=64, null=True)),
                ('company', models.CharField(blank=True, default='', help_text='公司名称', max_length=32, null=True)),
                ('address', models.CharField(blank=True, default='', help_text='地址', max_length=256, null=True)),
                ('mobile', models.CharField(blank=True, default='', help_text='手机号码', max_length=16, null=True)),
                ('phone', models.CharField(blank=True, default='', help_text='座机', max_length=16, null=True)),
                ('qq', models.CharField(blank=True, default='', help_text='QQ', max_length=16, null=True)),
                ('wechat', models.CharField(blank=True, default='', help_text='微信号', max_length=64, null=True)),
                ('web', models.CharField(blank=True, default='', help_text='网站地址', max_length=64, null=True)),
                ('industry', models.CharField(blank=True, default='', help_text='行业', max_length=32, null=True)),
                ('description', models.TextField(blank=True, default='', help_text='公司简介', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GetPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, help_text='积分值')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='积分获取时间')),
                ('reason', models.CharField(default='', help_text='获取原因', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0, help_text='余额')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='题纲', max_length=128)),
                ('index', models.IntegerField(db_index=True, default=0, help_text='题号')),
                ('category', models.CharField(choices=[('radio', '单选'), ('select', '多选')], default='radio', help_text='是否多选', max_length=16)),
                ('required_question', models.BooleanField(default=1, help_text='是否必答, 0→未答题,1→必答题')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='选项内容', max_length=32)),
                ('order_number', models.IntegerField(default=0, help_text='序号')),
                ('question', models.ForeignKey(help_text='题目', on_delete=django.db.models.deletion.CASCADE, to='question.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='标题', help_text='标题', max_length=64)),
                ('create_date', models.DateTimeField(auto_now=True, help_text='创建时间')),
                ('deadline', models.DateTimeField(auto_now=True, help_text='截止时间')),
                ('quantity', models.IntegerField(default=1, help_text='发布数量')),
                ('free_count', models.IntegerField(default=1, help_text='可用问卷数量')),
                ('state', models.IntegerField(default=0, help_text='状态, 0→草稿,1→待审核,2→审核失败,3→审核通过,4→已发布')),
                ('type', models.CharField(blank=True, default='', help_text='问卷类型', max_length=64, null=True)),
                ('customer', models.ForeignKey(help_text='客户信息', on_delete=django.db.models.deletion.CASCADE, to='question.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='审核时间')),
                ('comment', models.TextField(help_text='审核批注')),
                ('questionnaire', models.ForeignKey(help_text='问卷', on_delete=django.db.models.deletion.CASCADE, to='question.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='UsePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, help_text='积分值')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='积分获取时间')),
                ('reason', models.CharField(default='', help_text='积分使用原因', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='姓名', help_text='姓名', max_length=32)),
                ('age', models.IntegerField(default=1, help_text='年龄')),
                ('sex', models.BooleanField(default=1, help_text='性别, 0→女, 1→男')),
                ('phone', models.CharField(blank=True, default='', help_text='手机号码', max_length=16, null=True)),
                ('email', models.CharField(blank=True, default='', help_text='邮箱', max_length=64, null=True)),
                ('address', models.CharField(blank=True, default='', help_text='地址', max_length=256, null=True)),
                ('birthday', models.DateTimeField(default=datetime.date(2018, 1, 1), help_text='出生日期', null=True)),
                ('qq', models.CharField(blank=True, default='', help_text='QQ', max_length=16, null=True)),
                ('wechat', models.CharField(blank=True, default='', help_text='微信号', max_length=64, null=True)),
                ('job', models.CharField(blank=True, default='', help_text='职业', max_length=32, null=True)),
                ('hobby', models.CharField(blank=True, default='', help_text='兴趣爱好', max_length=64, null=True)),
                ('salary', models.CharField(blank=True, default='', help_text='收入水平', max_length=32, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, help_text='余额')),
                ('customer', models.OneToOneField(help_text='客户', on_delete=django.db.models.deletion.CASCADE, to='question.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='WalletInflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='交易时间')),
                ('amount', models.FloatField(default=0, help_text='发生金额')),
                ('consume_state', models.BooleanField(default=1, help_text='是否支付, 0→待支付,1→已支付')),
                ('recharge_type', models.CharField(choices=[('alipay', '支付宝'), ('wechat', '微信')], help_text='支付方式', max_length=32)),
                ('recharge_id', models.CharField(help_text='充值记录', max_length=128)),
                ('serial_number', models.CharField(help_text='消费流水号', max_length=128)),
                ('wallet', models.ForeignKey(help_text='钱包', on_delete=django.db.models.deletion.CASCADE, to='question.Wallet')),
            ],
        ),
        migrations.CreateModel(
            name='WalletOutflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, help_text='交易时间')),
                ('amount', models.FloatField(default=0, help_text='发生金额')),
                ('consume_state', models.BooleanField(default=1, help_text='是否支付, 0→待支付,1→已支付')),
                ('serial_number', models.CharField(help_text='消费流水号', max_length=128)),
                ('wallet', models.ForeignKey(help_text='钱包', on_delete=django.db.models.deletion.CASCADE, to='question.Wallet')),
            ],
        ),
        migrations.AddField(
            model_name='usepoint',
            name='userinfo',
            field=models.OneToOneField(help_text='用户信息', on_delete=django.db.models.deletion.CASCADE, to='question.UserInfo'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(help_text='问卷', on_delete=django.db.models.deletion.CASCADE, to='question.Questionnaire'),
        ),
        migrations.AddField(
            model_name='point',
            name='userinfo',
            field=models.OneToOneField(help_text='用户信息', on_delete=django.db.models.deletion.CASCADE, to='question.UserInfo'),
        ),
        migrations.AddField(
            model_name='getpoint',
            name='userinfo',
            field=models.OneToOneField(help_text='用户信息', on_delete=django.db.models.deletion.CASCADE, to='question.UserInfo'),
        ),
        migrations.AddField(
            model_name='answeritem',
            name='item',
            field=models.ForeignKey(help_text='选项', on_delete=django.db.models.deletion.CASCADE, to='question.QuestionItem'),
        ),
        migrations.AddField(
            model_name='answeritem',
            name='userinfo',
            field=models.ForeignKey(help_text='用户信息', null=True, on_delete=django.db.models.deletion.CASCADE, to='question.UserInfo'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionnaire',
            field=models.ForeignKey(help_text='问卷', on_delete=django.db.models.deletion.CASCADE, to='question.Questionnaire'),
        ),
        migrations.AddField(
            model_name='answer',
            name='userinfo',
            field=models.ForeignKey(help_text='用户信息', null=True, on_delete=django.db.models.deletion.CASCADE, to='question.UserInfo'),
        ),
    ]

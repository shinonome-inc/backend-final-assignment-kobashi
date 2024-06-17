from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tweets", "0002_alter_tweet_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tweet",
            options={"ordering": ["-created_at"]},
        )
    ]

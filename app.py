#!/usr/bin/env python
# coding: utf-8

# In[21]:


from textblob import TextBlob


# In[22]:


from flask import Flask


# In[23]:


from flask import render_template, request


# In[24]:


app = Flask(__name__)


# In[25]:


@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting...."))
    


# In[26]:


if __name__ == "__main__":
    app.run()


# In[ ]:





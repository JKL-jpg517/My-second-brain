---
banner: "https://i.postimg.cc/qvCj5L94/5bae6568ef880e422d97118ae7cc0afd.jpg"
cssclasses:
  - db-page
banner_y: 0.216
---

> [!db-blue] [[Academic/Academic Content&Progress|🎓 学业]]

> [!db-green] [[Reading/Reading Content&Progress|📚 阅读]]

> [!db-orange] [[Hobby/Hobby Content&Progress|📈 爱好]]

> [!db-purple] [[Journal/Journal Content&Progress|✍️ 日记]]

> [!db-panel]
> ### 🗓️ 今日任务
> ```dataview
> TASK
> WHERE !completed 
>   AND (due = date(today) OR file.day = date(today))
> SORT due ASC
> LIMIT 8
> ```

> [!db-panel]
> ### 📅 状态日历
> ```dataview
> calendar file.day
> ```
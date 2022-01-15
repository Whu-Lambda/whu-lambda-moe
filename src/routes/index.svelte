<script>
  import ArticleCard from '$lib/components/ArticleCard.svelte';
  import EventCard from '$lib/components/EventCard.svelte';
  import Apps from '$lib/components/Apps.svelte';

  export let articles = [
    {
      id: 1,
      name: ' “开源软件供应链点亮计划——暑期2021”项目提案',
      author: 'whu-lambda',
      created_at: '2022-01-15',
      cover: '',
      content:
        '项目简介今年，中科院软件所与华为 openEuler 项目继续共同举办 “开源软件供应链点亮计划——暑期2021” 项目。本次 TUNA 协会将继续作为社区加入这一计划，提供若干项目需求。欢迎有能力、有热情、有时间的小伙伴们参加，也欢迎 TUNA 成员们提出更多需求。TUNA 愿意和大家一起，为国内的开源生态添砖加瓦。2020 年，TUNA 基于自身与上游需求，共提出了涉及镜像站基础设施、应用软件移植与更新、发行版维护、性能优化等多个方面的 14 个项目，并有 ...'
    }
  ];

  export let events = [
    {
      id: 1,
      name: ' “开源软件供应链点亮计划——暑期2021”项目提案',
      time: '2022-01-15 18:30-20:30',
      place: '图书馆',
      status: '进行中',
      content:
        '项目简介今年，中科院软件所与华为 openEuler 项目继续共同举办 “开源软件供应链点亮计划——暑期2021” 项目。本次 TUNA 协会将继续作为社区加入这一计划，提供若干项目需求。欢迎有能力、有热情、有时间的小伙伴们参加，也欢迎 TUNA 成员们提出更多需求。TUNA 愿意和大家一起，为国内的开源生态添砖加瓦。2020 年，TUNA 基于自身与上游需求，共提出了涉及镜像站基础设施、应用软件移植与更新、发行版维护、性能优化等多个方面的 14 个项目，并有 ...'
    }
  ];
</script>

<div >
  <Apps />
</div>

<div class="row p-5">
  <div class="col-md-6">
    <h4>近期文章</h4>

    {#each articles as article, idx (idx)}
      <ArticleCard {article} />
    {/each}
  </div>
  <div class="col-md-6">
    <h4>近期活动</h4>

    {#each events as event, idx (idx)}
      <EventCard {event} />
    {/each}
  </div>
</div>

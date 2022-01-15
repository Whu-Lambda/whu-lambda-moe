<script>
  import EventCard from '$lib/components/EventCard.svelte';

  export let events = [
    {
      name: ' “开源软件供应链点亮计划——暑期2021”项目提案',
      time: '2022-01-15 18:30-20:30',
      place: '图书馆',
      status: '进行中',
      content:
        '“计算摄影（Computational Photography）”是近年来经常出现在各种“电话相机”发布会上的玄学名词。虽然我们小学二年级时就学过镜头成像原理，但在算法遍地开花的今天，一张高质量的朋友圈照骗早已不仅仅是光学成像的原始还原。毕业多年的炼丹师 bigeagle，常年穿梭于五彩斑斓的黑与明暗有致的白之间，本次 Tunight，他将为大家分享藏在拍照按钮背后的故事。\n活动信息：\n主讲人：汪彧之\n时间：2021/11/27（周六） 19:00 UTC +08:00\n活动形式：线下 + 线上会议 + 直播\n地点：三教 1202\n线上会议：Zoom 991 7605 1476 密码 211127\n直播链接：YouTube，开始后公布\n欢迎一起来玩！'
    },
    {
      name: ' “开源软件供应链点亮计划——暑期2021”项目提案',
      time: '2022-01-15 18:30-20:30',
      place: '图书馆',
      status: '进行中',
      content:
        '“计算摄影（Computational Photography）”是近年来经常出现在各种“电话相机”发布会上的玄学名词。虽然我们小学二年级时就学过镜头成像原理，但在算法遍地开花的今天，一张高质量的朋友圈照骗早已不仅仅是光学成像的原始还原。毕业多年的炼丹师 bigeagle，常年穿梭于五彩斑斓的黑与明暗有致的白之间，本次 Tunight，他将为大家分享藏在拍照按钮背后的故事。\n活动信息：\n主讲人：汪彧之\n时间：2021/11/27（周六） 19:00 UTC +08:00\n活动形式：线下 + 线上会议 + 直播\n地点：三教 1202\n线上会议：Zoom 991 7605 1476 密码 211127\n直播链接：YouTube，开始后公布\n欢迎一起来玩！'
    }
  ];
</script>

<div class="row justify-content-center">
  <div class="col-md-8">
    <h4>近期活动</h4>
    {#each events as event, idx (idx)}
      <EventCard {event} />
    {/each}
  </div>
</div>

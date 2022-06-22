<script>
    import { Swiper, SwiperSlide } from 'swiper/svelte';
    import SwiperCore, { Mousewheel, Pagination } from 'swiper';
    import 'swiper/css';
    import 'swiper/css/pagination';
    SwiperCore.use([Mousewheel, Pagination]);

    export let tracks;
</script>
<div class="tracks">
{#if tracks}
    <Swiper
    spaceBetween={50}
    slidesPerView={1}
    on:slideChange={() => console.log('slide change')}
    on:swiper={(e) => console.log(e.detail[0])}
    >
    {#each tracks as track, i}
        <SwiperSlide>
            <div class="track-holder">
                <div class="img-container" style="background-image:url('https://i.discogs.com/AuYj6MlGV2QY6O9uwJYxf281OLlHeYpPUw-v47gYzlY/rs:fit/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM5Njg0/MDItMTQ3MDM0Mzg4/MC01MzIyLmpwZWc.jpeg') ;"></div>
                <h2>{track.title}</h2>
                <audio controls id="current-track">
                <source src={track.url} type="audio/mpeg">
                </audio>
                <button class="has-pointer-event">+</button>
                <button class="has-pointer-event">-</button>
            </div>
        </SwiperSlide>
    {/each}
    </Swiper>
    {/if}
</div>

<style>

    h2 {
        text-align: left;
        font-size: 20px;   
    }

  .track-holder {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 30%;
    background-color: white;
    margin: auto;
    border-radius: 12px;
  }
  .img-container {
    background-image: url("https://i.discogs.com/AuYj6MlGV2QY6O9uwJYxf281OLlHeYpPUw-v47gYzlY/rs:fit/g:sm/q:40/h:300/w:300/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTM5Njg0/MDItMTQ3MDM0Mzg4/MC01MzIyLmpwZWc.jpeg");
    height: 300px;
    width: 100%;
    background-size: cover;
    border-radius: 12px;
  }

  
</style>
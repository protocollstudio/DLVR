<script>
	import { onMount } from "svelte";

  let apiUrl = "http://localhost:8000/api/"
  let tracks = []
  let currentTrack = []
  // when called make a DEL request to api/tracks/ with an object containing the track path
  const deleteTrack = (path) => {
    /*fetch(`http://localhost:4000/api/tracks/${path}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log(data)
      })*/
      console.log("Track deleted " + path)
      currentTrack = ({ "title": "So much juice in here", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", "path": "public/tracks/juice.mp3" })
      changeCurrentTime()
  }

  // when called make a get request to api/tracks/ and return the tracks
  const getTracks = () => {
    fetch(apiUrl + 'tracks', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log(data)
      })
      console.log("Tracks fetched")
      // append on top of the tracks array
      currentTrack = ({ "title": "So much juice in here", "url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3", "path": "public/tracks/juice.mp3" })
      changeCurrentTime()
  }

  // web called change media element current time
  const changeCurrentTime = () => {
    console.log("Current time changed")
    // change current time of media element
    let mediaElement = document.getElementById('current-track');
    mediaElement.currentTime = 60; //Skips to 122 seconds into the song

  }

  onMount(async () => {
			await fetch(apiUrl + 'tracks')
			.then(response => response.json())
			.then(datas => {
				console.log(datas);
        datas.forEach(data => {
          tracks = [data,...tracks]
        }); 
        console.log('track', tracks)
			}).catch(error => {
				console.log(error);
				return [];
			});
  })

  //console.log('currentTrack',currentTrack)
  let display = true
</script>

<main>
  {#if display}
    {tracks}
    {#each tracks as track}
        <div>
          <h1>{track?.title}</h1>
          <audio controls id="current-track">
            <source src={track?.url} type="audio/mpeg">
          </audio>
          <button on:click={() => getTracks()} >Like</button>
          <button on:click={() => deleteTrack(track?.path)}>Delete</button>
        </div>
    {/each}
	{/if}
</main>

<style>
  :root {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }

  img {
    height: 16rem;
    width: 16rem;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4rem;
    font-weight: 100;
    line-height: 1.1;
    margin: 2rem auto;
    max-width: 14rem;
  }

  p {
    max-width: 14rem;
    margin: 1rem auto;
    line-height: 1.35;
  }

  @media (min-width: 480px) {
    h1 {
      max-width: none;
    }

    p {
      max-width: none;
    }
  }
</style>

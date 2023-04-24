<script lang="ts">
	const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;
	const yt_embed_url = 'https://www.youtube.com/embed/';

	let info: {
		id: string;
		title: string;
		thumbnail: string;
		description: string;
		ext: string;
	};
	let url: string;
	let video_id: string;

	function getVideoId(url: string) {
		var valid_url_regex =
			/^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w-]+\?v=|embed\/|v\/)?)([\w-]+)(\S+)?$/gim;
		if (!valid_url_regex.test(url)) return '';

		var regExp = /^.*(youtu\.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
		var match = url.match(regExp);
		console.log('match', match);
		if (match && match[2].length == 11) {
			return match[2];
		} else {
			//error
			return '';
		}
	}

	function searchVideo() {
		video_id = getVideoId(url);
		if (!video_id) return;
	}

	async function downloadVideoInfo() {
		const response = await fetch(`${BACKEND_URL}/items/${video_id}`, {
			method: 'GET',
			headers: {
				'content-type': 'application/json'
			}
		});

		if (response.status !== 200) return alert('Error: ' + response.status);

		const response_json = await response.json();
		info = response_json.info;
	}

	// function formatName(format: typeof info.formats[0]) {
	// 	const has =
	// 		format.hasAudio && format.hasVideo
	// 			? 'Audio and Video'
	// 			: format.hasAudio
	// 			? 'Audio only'
	// 			: format.hasVideo
	// 			? 'Video only'
	// 			: 'No Audio or Video';
	// 	const mimeType = format.mimeType ? format.mimeType.split(';')[0] : '';

	// 	return `${has} (${mimeType})`;
	// }

	// function formatWithAudioVideo(data: typeof info) {
	// 	return data.formats.filter((f) => f.hasAudio && f.hasVideo)[0].url;
	// }
</script>

<div id="video-input">
	<input
		type="text"
		bind:value={url}
		placeholder="Youtube Video URL (e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
		pattern="^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
		required
	/>
	<button on:click={searchVideo}>Search</button>
</div>

<!-- {#if info}
	<div id="info">
		<ul class="formats">
			{#each info.formats as format}
				<li class="format-item">
					<span class="format-item-name">{formatName(format)}</span>
					<a class="format-item-url" href={format.url} rel="noreferer">DOWNLOAD</a>
				</li>
			{/each}
		</ul>
	</div>
{/if} -->

{#if video_id}
	<div id="video-frame">
		<iframe
			title="Youtube Embed"
			width="640"
			height="480"
			src={`${yt_embed_url}/${video_id}`}
		/>
	</div>
	<button on:click={downloadVideoInfo}>Download</button>
{/if}

{#if info}
	<div id="info">
		<p class="title">Video title: {info.title}</p>
		<p class="thumbnail">Video thumbnail: {info.thumbnail}</p>
		<p class="description">Video description: {info.description}</p>
		<p class="ext">Video extension: {info.ext}</p>
	</div>
{/if}

<style>
	#video-input {
		display: flex;
		flex-direction: column;
		width: 80%;
	}

	input:valid {
		background-color: palegreen;
	}

	input:invalid {
		background-color: lightpink;
	}

	/* .format-item {
		list-style: none;
		display: flex;
		flex-direction: row;
		justify-content: space-between;
	} */
</style>

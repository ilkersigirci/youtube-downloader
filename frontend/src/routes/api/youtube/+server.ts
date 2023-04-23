// TODO: Test and Made it functional
import { Router } from '@sveltejs/kit';
import ytdlp from 'yt-dlp';

export async function get({ query }: Router.Request) {
	const { q: searchQuery } = query;
	// Fetch video data from yt-dlp
	const videoData = await ytdlp.search(searchQuery);
	// Return the video data as JSON
	return {
		body: videoData,
		headers: {
			'Content-Type': 'application/json'
		}
	};
}

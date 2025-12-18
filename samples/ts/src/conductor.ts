import { Performer, HctSignal } from './performer';

async function main() {
    const saxophonist = new Performer("Saxophone");

    console.log("--- Movement 1: The Setup ---");
    await saxophonist.perform("Play intro", {
        signal: 'cue',
        performance: { tempo: 'andante', dynamics: 'mf' }
    });

    console.log("\n--- Movement 2: The Loop ---");
    // Attacca means go immediately from previous
    await saxophonist.perform("Improvise", {
        signal: 'vamp',
        performance: { tempo: 'allegro', dynamics: 'f' }
    });

    console.log("\n--- Finale ---");
    await saxophonist.perform("Hold final note", {
        signal: 'fermata',
        performance: { tempo: 'largo', dynamics: 'ff' }
    });
}

main().catch(console.error);

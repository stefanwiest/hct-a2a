export interface HctSignal {
    signal: 'cue' | 'fermata' | 'attacca' | 'vamp' | 'caesura';
    performance?: {
        tempo?: 'largo' | 'andante' | 'moderato' | 'allegro' | 'presto';
        dynamics?: 'pp' | 'p' | 'mf' | 'f' | 'ff';
    };
}

export class Performer {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    async perform(action: string, hct: HctSignal): Promise<string> {
        const tempo = hct.performance?.tempo || 'moderato';
        const dynamics = hct.performance?.dynamics || 'mf';

        console.log(`[${this.name}] Received ${hct.signal.toUpperCase()} | Tempo: ${tempo} | Dynamics: ${dynamics}`);

        // Logic based on Signals
        if (hct.signal === 'vamp') {
            console.log(`[${this.name}] Vamping (looping) on "${action}"...`);
            await this.sleep(500);
            console.log(`[${this.name}] ...Vamp complete.`);
        } else if (hct.signal === 'caesura') {
            console.log(`[${this.name}] CAESURA! Stopping immediately.`);
            return "Stopped.";
        }

        // Logic based on Dynamics
        let cost = 1;
        if (dynamics === 'ff') cost = 5;
        if (dynamics === 'pp') cost = 0.1;

        console.log(`[${this.name}] Executing "${action}" with cost factor ${cost}`);

        return "Done";
    }

    private sleep(ms: number) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

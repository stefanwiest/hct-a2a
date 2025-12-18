use serde::{Deserialize, Serialize};
use std::time::Duration;
use tokio::time::sleep;

#[derive(Debug, Serialize, Deserialize)]
struct HctSignal {
    signal: SignalType,
    #[serde(default)]
    performance: PerformanceDetails,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
enum SignalType {
    Cue,
    Fermata,
    Attacca,
    Vamp,
    Caesura,
    Downbeat,
}

#[derive(Debug, Serialize, Deserialize, Default)]
struct PerformanceDetails {
    #[serde(default = "default_tempo")]
    tempo: Tempo,
    #[serde(default = "default_dynamics")]
    dynamics: Dynamics,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
enum Tempo {
    Largo,
    Andante,
    Moderato,
    Allegro,
    Presto,
}

#[derive(Debug, Serialize, Deserialize)]
#[serde(rename_all = "lowercase")]
enum Dynamics {
    Pp,
    P,
    Mf,
    F,
    Ff,
}

fn default_tempo() -> Tempo { Tempo::Moderato }
fn default_dynamics() -> Dynamics { Dynamics::Mf }

async fn performer(name: String, mut rx: tokio::sync::mpsc::Receiver<HctSignal>) {
    while let Some(hct) = rx.recv().await {
        println!("[{}] Received {:?} | Tempo: {:?} | Dynamics: {:?}", 
            name, hct.signal, hct.performance.tempo, hct.performance.dynamics);
        
        match hct.signal {
             SignalType::Downbeat => {
                 println!("[{}] DOWNBEAT - Syncing global state...", name);
             },
             _ => {}
        }
    }
}

#[tokio::main]
async fn main() {
    let (tx, rx) = tokio::sync::mpsc::channel(32);

    // Spawn Performer
    tokio::spawn(performer("RustEnsemble".to_string(), rx));

    // Conductor actions
    let signals = vec![
        HctSignal { 
            signal: SignalType::Cue, 
            performance: PerformanceDetails { tempo: Tempo::Allegro, dynamics: Dynamics::Mf } 
        },
        HctSignal { 
            signal: SignalType::Downbeat, 
            performance: PerformanceDetails { tempo: Tempo::Presto, dynamics: Dynamics::Ff } 
        }
    ];

    for signal in signals {
        tx.send(signal).await.unwrap();
        sleep(Duration::from_millis(500)).await;
    }
}

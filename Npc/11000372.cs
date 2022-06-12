using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000372: Dr. Mikhail
/// </summary>
public class _11000372 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001526$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001529$
                // - As scientists, we must always look toward the future. We must not abandon our research because we aren't happy with the immediate results, or out of fear of perceived consequences. Science requires persistence and dedication!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

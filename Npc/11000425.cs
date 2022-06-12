using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000425: Loki
/// </summary>
public class _11000425 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001772$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001774$
                // - These vultures are not tamed. What if they fly me to some unfamiliar place or drop me in midair?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

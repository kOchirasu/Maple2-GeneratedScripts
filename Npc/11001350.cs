using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001350: Oliver Olivieta
/// </summary>
public class _11001350 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005313$
    // - Good. Right. Perfect!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005316$
                // - Yeeees? It's rude to barge in on someone's summer home, you know. Please remove yourself from the premises.
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

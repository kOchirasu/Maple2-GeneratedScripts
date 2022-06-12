using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001318: Kabo
/// </summary>
public class _11001318 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005037$
    // - Do you need help?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005704$
                // - The greatest threat is the one we do not see. We need divine guidance to find our path.
                return 40;
            case (40, 1):
                // $script:1227194507005705$
                // - We humans are weak and hopeless, but we have a will that is stronger than steel.
                return 40;
            case (40, 2):
                // $script:1227194507005706$
                // - The divine recognizes this and guides our hand. Remember that, and you will never know fear.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

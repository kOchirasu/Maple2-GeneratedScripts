using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003156: Pippy
/// </summary>
public class _11003156 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0306155707008047$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0306155707008049$
                // - I know, right? All three of us are pretty, but the prettiest one is... oh, you were talking about the flowers. Sure, they're pretty too! Ah, forget what I said earlier.
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

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001046: Hatar
/// </summary>
public class _11001046 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407003573$
    // - I'm sensing evil energy... The kind that can never be purged... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407003577$
                // - I came all the way here to clear my head and focus on my training. I don't know how so many people have heard about my lava-reading skill. I would send them away, but I respect their determination to come all the way out here.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001062: Nox
/// </summary>
public class _11001062 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180306000378$
    // - You must be here to see me.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1208032606000568$
                // - Mm? Is there something you'd like to trade?
                switch (selection) {
                    // $script:1208032606000569$
                    // - I heard you collect $itemPlural:40100024$.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1208032606000570$
                // - You're pretty lucky if you find $itemPlural:40100024$, but I can't help you. I'm actually out of business. If you want to buy items, you'll have to shop elsewhere.
                switch (selection) {
                    // $script:1208032606000571$
                    // - You're out of business?!
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1208032606000572$
                // - Why does any businessman go out of business? I'm not making enough profit.
                return 42;
            case (42, 1):
                // $script:1208032606000573$
                // - I'll either have to start selling different products or stop selling altogether...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

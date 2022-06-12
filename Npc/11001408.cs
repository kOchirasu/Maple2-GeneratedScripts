using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001408: Dali
/// </summary>
public class _11001408 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1217205907005405$
    // - Welcome to <i>our</i> territory, human. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1222203907005480$
                // - We don't usually let our clients in here. Seeing us train and tend to our wounded makes them realize that we, too, are mortal. It's bad for the brand, see?
                return 40;
            case (40, 1):
                // $script:1222203907005481$
                // - We like humans, of course, but we know better than to count them as friends. We once relied on our humans for happiness. That... didn't end well for us.
                return 40;
            case (40, 2):
                // $script:1222203907005482$
                // - Anyway, now that you've seen our base, you have to promise never to tell anyone about it. Only you and your closest friends are welcome here.
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

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003258: Kaitlyn
/// </summary>
public class _11003258 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008191$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008192$
                // - This is why I don't like kids. They want to be heroes, but they can't even tie their shoes on their own.
                return 30;
            case (30, 1):
                // $script:0403155707008193$
                // - But don't you think Professor $npcName:11003251[gender:0]$ is looking especially good lately? His skin has taken on a beautiful pasty sheen from all his hard work. I could stare at him all day...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

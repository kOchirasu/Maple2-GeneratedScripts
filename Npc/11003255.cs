using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003255: Kaitlyn
/// </summary>
public class _11003255 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008178$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008179$
                // - There's no shame in asking for my help. I am, after all, the smartest person you know.
                return 30;
            case (30, 1):
                // $script:0403155707008180$
                // - When you're done here, go ahead and help Professor $npcName:11003148[gender:0]$ with his research. He's been on edge lately thanks to his migraines. Don't do anything to make them worse, will you?
                return 30;
            case (30, 2):
                // $script:0403155707008181$
                // - <font color="#909090">($npcName:11003254[gender:1]$ whispers to herself.) </font>
                //   <font size='20'>I wish he wore glasses. He's so intelligent and sensitive... It would be perfect...</font>
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

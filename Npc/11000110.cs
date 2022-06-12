using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000110: Cavan
/// </summary>
public class _11000110 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;50
    }

    // Select 0:
    // $script:0831180407000449$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000452$
                // - At least it's good to be on this big lump of land instead of that small island. I felt so trapped there. 
                return -1;
            case (50, 0):
                // $script:0831180407000453$
                // - Hey, did you see that $npcName:22300149$ over there? I thought they only had those in my hometown. I had no idea!
                return 50;
            case (50, 1):
                // $script:0831180407000454$
                // - Anything that reminds me of my hometown makes me happy. Like that $npcName:22300149$... I guess this is what it's like to be homesick. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

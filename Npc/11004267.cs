using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004267: Sunny
/// </summary>
public class _11004267 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011217$
    // - Welcome to $map:02010012$! I'm $npcName:11004267[gender:1]$, the spokeswoman! Or at least, I will be, when the place finally opens...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011218$
                // - Welcome to $map:02010012$! I'm $npcName:11004267[gender:1]$, the spokeswoman! Or at least, I will be, when the place finally opens...
                switch (selection) {
                    // $script:0911203207011219$
                    // - When is this place gonna open?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011220$
                // - That's what I wanna know, too! I heard there's some kinda bug problem holding up the construction...
                return 11;
            case (11, 1):
                // $script:0911203207011221$
                // - But honestly, they tell me I have the job, so shouldn't they open so I can start working? I already spent a fortune promoting myself... Anyway, remember my name, and watch as I become the best model in all Karkar!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

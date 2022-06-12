using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003507: Karyan
/// </summary>
public class _11003507 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0816160115009007$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0816160115009008$
                // - I'm a member of Team Mushroom, but I'm also a freelance pet-tamer.
                switch (selection) {
                    // $script:0816160115009009$
                    // - Can I hire you?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0816160115009010$
                // - Not now. I'm on vacation.
                return -1;
            case (40, 0):
                // $script:0816211415009058$
                // - Apparently, Dryad Co. set their R&D department loose on monsters' tastebuds and developed these new monster candies. The $itemPlural:63000000$ are pretty popular.
                switch (selection) {
                    // $script:0816211415009059$
                    // - Where can I get these monster candies?
                    case 0:
                        return 41;
                    // $script:0816211415009060$
                    // - Tell me about Dryad Co.
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0816211415009061$
                // - Most major supply shops should carry $itemPlural:63000000$. I'm pretty sure $npcName:11003506[gender:1]$ has some in stock.
                return -1;
            case (42, 0):
                // $script:0816211415009062$
                // - I don't really know much, myself. It's a tech giant with lots of next-gen products. Rumor has it one of the founders of Dryad Co. recently retired, but nobody really knows much about them, or even what they look like.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

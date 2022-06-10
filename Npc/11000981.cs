using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000981: Christopher
/// </summary>
public class _11000981 : NpcScript {
    internal _11000981(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610001130$ 
                // - Ahoy! 
                return true;
            case 1:
                // $script:0831180610001131$ 
                // - The Marco has a noble purpose, to transport adventurers on missions for the $map:02000068$. And lately, it's also been carrying adventurers to $map:02000183$ where they battle pirates in the eastern straits. If you're one of these adventurers, then you can board the ship for 4,000 mesos. Is that what you want to do?
                return true;
            case 40:
                // $script:0831180610001135$ 
                // - You need something?
                switch (selection) {
                    // $script:0831180610001136$
                    // - Can I board the ship?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180610001137$
                    // - I'm just looking around.
                    case 1:
                        Id = 42;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180610001138$ 
                // - The <i>Marco</i> only transports adventurers who are carrying out special missions in $map:02000068$. Other adventurers and ordinary civilians can't board.
                return true;
            case 42:
                // $script:0831180610001139$ 
                // - Taking a break from adventuring, eh? Nice. Wish I could do that, but this dock isn't going to manage itself.
                return true;
            case 50:
                // $script:0831180610001140$ 
                // - The operation of the Marco is mostly paid by the $map:02000068$, so the passengers only pay a small fare of 4,000 mesos. If you want to board, that's your price.
                return true;
            default:
                return true;
        }
    }
}

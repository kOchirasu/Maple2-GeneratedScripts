using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000401: Melson
/// </summary>
public class _11000401 : NpcScript {
    internal _11000401(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001623$ 
                // - How may I help you? 
                return true;
            case 20:
                // $script:0831180407001625$ 
                // - Please be very careful with this. It's one of my all-time favorite comic books. 
                return true;
            case 30:
                // $script:0831180407001626$ 
                // - $male:Mister,female:Lady$, do you like comic books? They're my favorite thing in the world. I want to be an illustrator when I grow up. 
                return true;
            default:
                return true;
        }
    }
}

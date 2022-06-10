using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001520: Swordsman
/// </summary>
public class _11001520 : NpcScript {
    internal _11001520(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515211707006107$ 
                // - Nice to meet you!
                return true;
            case 10:
                // $script:0515211707006108$ 
                // - I'm honored to join the Starlight Expedition. The captain of the guard sent me to help $npc:11000076[gender:0]$. I intend to win glory for the guard!
                return true;
            default:
                return true;
        }
    }
}

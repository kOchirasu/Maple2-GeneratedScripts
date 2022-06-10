using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004235: Blackeye
/// </summary>
public class _11004235 : NpcScript {
    internal _11004235(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010923$ 
                // - I cannot fathom how much more powerful you'll grow.
                return true;
            case 10:
                // $script:0809223207010924$ 
                // - I cannot fathom how much more powerful you'll grow.
                // $script:0809223207010925$ 
                // - It's an honor to be working by your side once more, friend.
                return true;
            default:
                return true;
        }
    }
}

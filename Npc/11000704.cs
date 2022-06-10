using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000704: Rove
/// </summary>
public class _11000704 : NpcScript {
    internal _11000704(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002833$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:0831180407002834$ 
                // - Come to sample our juice? $npcName:11000445[gender:1]$ right here will set you up. Hope you're ready for a trip to flavor country! 
                return true;
            default:
                return true;
        }
    }
}

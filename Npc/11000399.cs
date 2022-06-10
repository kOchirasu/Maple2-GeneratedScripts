using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000399: Dr. Robson
/// </summary>
public class _11000399 : NpcScript {
    internal _11000399(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001616$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407001618$ 
                // - The more I think about it, the angrier I get! How could they stop me from going on vacation, and one that I've had planned for months? Maybe I should just leave and let them deal with the water.
                return true;
            default:
                return true;
        }
    }
}

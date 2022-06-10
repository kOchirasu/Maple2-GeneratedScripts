using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000266: Jin
/// </summary>
public class _11000266 : NpcScript {
    internal _11000266(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001085$ 
                // - What brings you here? 
                return true;
            case 20:
                // $script:0831180407001087$ 
                // - Captain $npcName:11000044[gender:0]$ commands Dark Wind now, but before the Blue Lapenta broke we were led by Winn Stilton. Every member of Dark Wind, myself included, considered Captain Stilton a true hero. 
                // $script:0831180407001088$ 
                // - That's why we can never forgive $npcName:11000064[gender:0]$! He not only destroyed the Blue Lapenta, but he also killed Captain Stilton! 
                return true;
            case 30:
                // $script:0831180407001089$ 
                // - I can't believe $npcName:11000044[gender:0]$ ended Captain Stilton's life. That brazen coward fooled us all! 
                return true;
            default:
                return true;
        }
    }
}

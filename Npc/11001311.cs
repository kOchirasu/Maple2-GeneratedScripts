using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001311: Ronan
/// </summary>
public class _11001311 : NpcScript {
    internal _11001311(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005030$ 
                // - Glory to the empress! 
                return true;
            case 30:
                // $script:1227194507005664$ 
                // - I've never been this far from home before. I miss my family... 
                // $script:1227194507005665$ 
                // - My friends envied me for getting to go on this trip. I was excited, too. But the day before I left, I was already feeling homesick. 
                // $script:1227194507005666$ 
                // - You're amazing, you know that? You've been far from home even longer than I have, and it doesn't show. I've got to work to be as strong as you someday! 
                return true;
            default:
                return true;
        }
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004289: Beaumarchais
/// </summary>
public class _11004289 : NpcScript {
    internal _11004289(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0921211107011340$ 
                // - For such an old hotel, I suppose this place has its charm. 
                return true;
            case 10:
                // $script:0921211107011341$ 
                // - My cousin certainly devoted enough time and money to this place. He passed the hotel to me when he died, but I simply have no interest in running it. 
                return true;
            default:
                return true;
        }
    }
}

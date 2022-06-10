using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004224: Richelle
/// </summary>
public class _11004224 : NpcScript {
    internal _11004224(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010796$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:0806222707010797$ 
                // - Hey, thanks for listening! We're Riot at the Danceclub. We all met during an audition and decided to form a band, kindred spirits and all that. We picked stage names to riff off the band name.
                return true;
            default:
                return true;
        }
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004487: Diversi
/// </summary>
public class _11004487 : NpcScript {
    internal _11004487(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012284$ 
                // - Ah, the hero of Sky Fortress! You have many fans, you know. 
                return true;
            case 10:
                // $script:1227192907012285$ 
                // - Ah, the hero of Sky Fortress! You have many fans, you know. 
                switch (selection) {
                    // $script:1227192907012286$
                    // - Stop. You're making me blush.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012287$ 
                // - Don't let it get to your head. You'll get sloppy. 
                // $script:1227192907012288$ 
                // - Anyway, this looks to be some kind of aetherine mine. There must be a huge deposit of the stuff under here. 
                // $script:1227192907012289$ 
                // - That would explain why there are so many enemy forces marshaled here. They want the aetherine. 
                // $script:1227192907012290$ 
                // - I think <i>we</i> ought to put our hat in the ring, so I sent a request for reinforcements. I'm trying to estimate the size of the aetherine deposit before they get here... 
                return true;
            default:
                return true;
        }
    }
}

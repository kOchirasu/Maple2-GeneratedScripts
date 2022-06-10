using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004481: Macrandra
/// </summary>
public class _11004481 : NpcScript {
    internal _11004481(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012212$ 
                // - Hm? I didn't expect to see anyone outside the safety of the outpost. 
                return true;
            case 10:
                // $script:1227192907012213$ 
                // - Hm? I didn't expect to see anyone outside the safety of the outpost. 
                switch (selection) {
                    // $script:1227192907012214$
                    // - What are you doing here?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012215$ 
                // - Oh, well I was sent out to look for aetherine samples, but I found this weird machine. I'm pretty sure it's related to aetherine somehow, but I haven't quite worked it out. 
                // $script:1227192907012216$ 
                // - It's weak, but that ring is drawing aetherine power into its center. I took some initial scans, and I think it's actually capable of storing vast amounts of the stuff. 
                switch (selection) {
                    // $script:1227192907012217$
                    // - That's strange.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012218$ 
                // - Isn't it? But I have theories! 
                // $script:1227192907012219$ 
                // - Based on the data I've collected so far, I have two ideas. Either this device is gathering aetherine and transporting it somewhere... 
                // $script:1227192907012220$ 
                // - Or it's a dimensional portal that's connected to a place far, far away. 
                // $script:1227192907012221$ 
                // - What kind of people live here, that they can make all this wild technology? 
                return true;
            default:
                return true;
        }
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003180: Marco
/// </summary>
public class _11003180 : NpcScript {
    internal _11003180(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0316101907008107$ 
                // - All's well! 
                return true;
            case 30:
                // $script:0323170507008126$ 
                // - You don't look like the usual beach bums we get around here. What do you want? 
                switch (selection) {
                    // $script:0426090007008442$
                    // - I'm part of the caravan escort.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0426090007008443$
                    // - I'm just passing through.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0426090007008444$ 
                // - You're just in time! Check in with the others in the $map:52000116$ behind me. 
                return true;
            case 32:
                // $script:0426090007008445$ 
                // - You're a tourist? Oh, okay. In that case, enjoy your stay. I'm new to this whole guardsman thing, so I wasn't sure what you were up to. Now I know you're cool, so... cool! 
                switch (selection) {
                    // $script:0426090007008446$
                    // - Thank you.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0426090007008447$ 
                // - Just doing my job, $male:sir,female:ma'am$! But it does feel good to be thanked. I wish more folk were like you. 
                return true;
            default:
                return true;
        }
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000412: 50 Meso
/// </summary>
public class _11000412 : NpcScript {
    internal _11000412(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001737$ 
                // - Wassup? 
                return true;
            case 20:
                // $script:0831180407001739$ 
                // - Sup, man? You wanna talk art? What do you think is the soul of art? 
                switch (selection) {
                    // $script:0831180407001740$
                    // - I don't... know?
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0831180407001741$
                    // - Heart
                    case 1:
                        Id = 22;
                        return false;
                    // $script:0831180407001742$
                    // - Talent
                    case 2:
                        Id = 23;
                        return false;
                    // $script:0831180407001743$
                    // - Swag
                    case 3:
                        Id = 24;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407001744$ 
                // - Then lemme educate you, man! A real artist uses their tools to show the world their heart. That's the whole point, yo! 
                return true;
            case 22:
                // $script:0831180407001745$ 
                // - That's right! You're on point today! 
                return true;
            case 23:
                // $script:0831180407001746$ 
                // - Talent? Man, anyone can train up talent. That's not what's important.  
                return true;
            case 24:
                // $script:0831180407001747$ 
                // - Seriously? Man, I don't want to talk to you anymore. 
                return true;
            default:
                return true;
        }
    }
}

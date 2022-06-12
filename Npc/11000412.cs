using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000412: 50 Meso
/// </summary>
public class _11000412 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001737$
    // - Wassup?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001739$
                // - Sup, man? You wanna talk art? What do you think is the soul of art?
                switch (selection) {
                    // $script:0831180407001740$
                    // - I don't... know?
                    case 0:
                        return 21;
                    // $script:0831180407001741$
                    // - Heart
                    case 1:
                        return 22;
                    // $script:0831180407001742$
                    // - Talent
                    case 2:
                        return 23;
                    // $script:0831180407001743$
                    // - Swag
                    case 3:
                        return 24;
                }
                return -1;
            case (21, 0):
                // $script:0831180407001744$
                // - Then lemme educate you, man! A real artist uses their tools to show the world their heart. That's the whole point, yo!
                return -1;
            case (22, 0):
                // $script:0831180407001745$
                // - That's right! You're on point today!
                return -1;
            case (23, 0):
                // $script:0831180407001746$
                // - Talent? Man, anyone can train up talent. That's not what's important. 
                return -1;
            case (24, 0):
                // $script:0831180407001747$
                // - Seriously? Man, I don't want to talk to you anymore.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            (24, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000219: Lucia
/// </summary>
public class _11000219 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000956$
    // - Wah! Geez!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000959$
                // - Argh, what?
                switch (selection) {
                    // $script:0831180407000960$
                    // - What are you doing?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000961$
                // - Sheesh, I don't know. I can't talk. Doing this is tough as it is. My limbs are so numb I can't feel them anymore. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

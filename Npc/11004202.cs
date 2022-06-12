using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004202: Tourist
/// </summary>
public class _11004202 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010652$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010653$
                // - Y'know, I wasn't so sure about those mushfolk when I got the brochure, but I've gotta say this place is pretty great!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

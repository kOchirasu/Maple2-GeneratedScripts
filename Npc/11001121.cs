using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001121: Dr. Collins
/// </summary>
public class _11001121 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0910171307003826$
    // - What brings you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915113107003927$
                // - Those on the cutting edge of technological research often complain about lack of funds, resources, and other material things. The only thing I lack is time... Say, how old do you think I am?
                switch (selection) {
                    // $script:0915113107003928$
                    // - You look young-ish to me.
                    case 0:
                        return 31;
                    // $script:0915113107003929$
                    // - You look like an old geezer. 50-plus, at least.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0915113107003930$
                // - Hmph! Flattery will get you nowhere with me. Or perhaps you need to see an eye doctor.
                return -1;
            case (32, 0):
                // $script:0915113107003931$
                // - Close enough! There's so much I want to study, but I'm past my prime. <i>If only there were more time...!</i> Wait... That gives me an idea...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001177: Gomei
/// </summary>
public class _11001177 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1012113807004092$
    // - Nothing to report, $male:sir,female:ma'am$.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1012113807004095$
                // - I'm fairly new to the Green Hoods, but I've been stationed here long enough to get the lay of the land. If something happens in $map:02000057$, I'll be the first to know. But, ah, let me know if you see anything suspicious anyway.
                switch (selection) {
                    // $script:1012113807004096$
                    // - How do you like being a member of the militia?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1012113807004097$
                // - Well, I've learned a lot of things. Like how being a guard means learning how to think on your feet. I'm not so great at that now, but I try hard.
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

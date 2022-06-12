using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000317: Jonn
/// </summary>
public class _11000317 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001205$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001209$
                // - Ah, are you an adventurer? So am I!
                switch (selection) {
                    // $script:0831180407001210$
                    // - Don't you lie to me!
                    case 0:
                        return 41;
                    // $script:0831180407001211$
                    // - What is an adventurer to you?
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001212$
                // - I-I'm not lying! I mean it!
                switch (selection) {
                    // $script:0831180407001213$
                    // - What do you think an adventurer is?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0831180407001214$
                // - An adventurer is someone who embarks on adventures around the world! I've even been to $map:02000023$, you know. My next destination is $map:02000051$!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

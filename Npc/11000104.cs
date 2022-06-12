using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000104: Santiago
/// </summary>
public class _11000104 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000425$
    // - Hey there!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000428$
                // - Well aren't you a sight for sore eyes. It's been a while since I've seen anybody that wasn't a skeleton or an angry octo-thing looking to bludgeon me to death.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}

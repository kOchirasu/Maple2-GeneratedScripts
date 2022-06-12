using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000201: Noel
/// </summary>
public class _11000201 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000874$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000877$
                // - Hey $male:mister,female:lady$, do you want to play with us too? I have to play while I can. My mom will be here soon to pick me up.
                return -1;
            case (40, 0):
                // $script:0831180407000878$
                // - I can't believe how big this field is! The sunlight stings a little bit, but Mom said a little sun is good for you.
                return 40;
            case (40, 1):
                // $script:0831180407000879$
                // - $map:02000023$ is nice and shady. Neal's going to come over to my house later. $male:Mister,female:Lady$, do you want to come?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
